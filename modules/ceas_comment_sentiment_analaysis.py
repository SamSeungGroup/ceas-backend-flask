import torch
from torch.utils.data import Dataset
import gluonnlp as nlp
import pandas as pd

from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model

from modules.ceas_kobert_module import BERTDataset, BERTClassifier

def comment_sentiment_analysis(comment_content):
    # 단어사전, 토크나이저 불러오기
    bertmodel, vocab = get_pytorch_kobert_model(cachedir=".cache")
    tokenizer = get_tokenizer()
    tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

    # Setting parameters
    max_len = 64

    # 모델 불러오기
    device = torch.device('cpu')

    # bertmodel.load_state_dict(torch.load('best_weights_v1.pt', map_location=device), strict=False)
    # bertmodel.eval()

    model = BERTClassifier(bertmodel,  dr_rate=0.5).to(device)
    model.load_state_dict(torch.load('models/best_weights_v1.pt', map_location='cpu'))
    model.eval()

    # loaded_model = torch.load('best_v2.pt', map_location=device)
    # loaded_model.eval()

    # 테스트 문장 예측
    test_sentence = comment_content
    test_label = 1 # 실제 정답

    unseen_test = pd.DataFrame([[test_sentence, test_label]], columns = [['document', 'label']])
    test_set = BERTDataset(unseen_test, 1, 2, tok, max_len, True, False)
    test_input = torch.utils.data.DataLoader(test_set, batch_size=1, num_workers=0)

    for token_ids, valid_length, segment_ids, label in test_input:
        token_ids = token_ids.long()
        segment_ids = segment_ids.long()
        valid_length= valid_length
        out = model(token_ids, valid_length, segment_ids)

    result = torch.nn.functional.softmax(out, dim=1)
    comment_positive, comment_negative = round(result[0][1].item(),3), round(result[0][0].item(),3)
    final_positive = comment_positive if comment_positive>=0.5 else -comment_negative

    return {
        'comment_positive': comment_positive
    }

if __name__ == '__main__':
    print(comment_sentiment_analysis('너무 비싸요'))