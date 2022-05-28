const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const ARTICLES = 'articles/'
const MOVIES = 'movies/'
const COMMENTS = 'comments/'
export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
    follow: username => HOST + ACCOUNTS + 'follow/' + `${username}/`,
    img: username => HOST + ACCOUNTS + 'upload_img/' + `${username}/`,
  },
  articles: {
    // /articles/
    articles: () => HOST + ARTICLES,
    // /articles/1/
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
    likeComment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/` + 'like/'
  },
  movies: {
    movie: movie_id => HOST + MOVIES + `${ movie_id }/`,
    movie_comment: movie_id => HOST + MOVIES + `${ movie_id }/` + COMMENTS,
    movie_comment_delete: (moviePk, commentPk) => HOST + MOVIES + `${moviePk}/` + COMMENTS + `${commentPk}/`,
    likeMovie: moviePk => HOST + MOVIES + `${ moviePk }/` + 'like/'
    // movies: () => HOST + MOVIES,
  }
}
