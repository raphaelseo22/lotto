# 로또 번호 예측
- 동행복권 API를 활용하여 역대 로또 당첨 번호를 크롤링
- 크로링한 번호를 바탕으로 가장 적은 번호들로 이루어진 예상 당첨 번호 1개 예측
- 선형회귀를 활용하여 예상 당첨 번호 1개 예측 -> X
  - 데이터 확인 결과 선형성이 보이지 않음
  - 가장 많이 나온 번호 6개를 예측값으로 사용
- 무작위 당첨 번호 3개 예측