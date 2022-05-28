import os
import requests
import json


TMDB_API_KEY = str(os.getenv('TMDB_API_KEY'))

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 501):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        print(request_url)
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movies_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\\t", ensure_ascii=False)

get_movie_datas()













































# class URLMaker():
#     # base_url 설정 - 클래스 변수 : 클래스 사용 내내 고정된 값 - 모든 클래스에서 공유 가능
#     base_url = 'https://api.themoviedb.org/3'

#     # 생성자 - api_key를 인스턴스 변수로 초기화하여 생성
#     def __init__(self, key):
#         self.key = key

#     # 인스턴스 메서드
#     # url 반환 
#     def get_url(self, category, feature, **kwargs): # param으로 가변인자로 받아온다. - query string방식 이용을 위해
#         # - class 속성인 base_url에 접근
#         # - category, feature는 인스턴스에 할당되어 있는 변수가 아닌
#         #   함수의 인자 argument로 들어온 값이기 때문에 self.변수명 형태가 아니라
#         #   인자값(아규먼트값)을 바로 사용한다.
#         url = f'{URLMaker.base_url}/{category}/{feature}'

#         # 인스턴스 생성 시, 인스턴스 변수로 저장된 api_key 값을 받아온다.
#         url += f'?api_key={self.key}'

#         # 가변인자로 받아온 값을 쿼리스트링 방식으로 url에 이어준다.
#         for key, value in kwargs.items():
#             url += f'&{key}={value}'

#         return url

#     # 인스턴스 메서드
#     # 영화 제목을 입력받아 영화 아이디를 반환
#     # - 요청으로 받을 응답에 영화정보 데이터(json)가 있을 것이고, 그 id를 반환해줄 것이다.
#     def movie_id(self, title):

#         # 인스턴스 메서드인 get_url() 호출 (self/movie는 영화제목을 받아 영화정보를 반환)
#         # - title을 입력하면 해당 영화제목에 맞는 영화 정보 url을 반환해준다.
#         url = self.get_url('search', 'movie', region='KR', language='ko', query=title)

#         # 만들어진 url을 통해 서버에 요청해, 응답을 받아온다.
#         response = requests.get(url)
        
#         # 받아온 데이터를 json -> dict으로 변환해준다.
#         movie_dict = response.json()

#         print(movie_dict)
#         # 만약 영화 제목에 해당하는 값이 있다면 
#         if movie_dict.get('results'):
#             # movie_dict에서 movie_id를 추출한다.
#             result = movie_dict.get('results')[0].get('id')
#             # 영화 제목에 해당하는 id 반환
#             return result
#         # 해당하는 값이 없다면, - result가 비어있다면
#         else:
#             return None  # None을 출력한다.

# # maker = URLMaker('[api_key]')
# # maker = URLMaker('b8f9b2d0a922278766b869e7acfc5f40')
# maker = URLMaker( os.getenv('TMDB_API_KEY') )
# # print(maker.get_url('movie', 'popular', region='KR', language='ko'))
# print(maker.movie_id('The Godfather'))