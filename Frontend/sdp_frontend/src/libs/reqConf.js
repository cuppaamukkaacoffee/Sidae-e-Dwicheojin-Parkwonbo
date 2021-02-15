export const apiHost = 'http://localhost/v1';

export const urls = {
  users: apiHost + '/users',
};

export const jsonHeader = () => {
  return {
    headers: {
      'Content-Type': 'application/json',
    },
  };
};

export const naverNewsHeader = () => {
  return {
    headers: {
      'Content-Type': 'application/json',
      'X-Naver-Client-Id': 'kSZmYJJptfOqxc32IsIH',
      'X-Naver-Client-Secret': 'TAs1DQc46o'
    }
  }
}

// 일반유저
export const jsonUserTokenHeader = (token) => {
  return {
    headers: {
      'Content-Type': 'application/json',
      'user-token': token,
    },
  };
};