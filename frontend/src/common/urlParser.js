export default {
  parseLimitOffPagination(url) {
    const args = url.slice(url.indexOf('?') + 1);
    const searchParams = new URLSearchParams(args);
    return {
      limit: searchParams.get('limit'),
      offset: searchParams.get('offset'),
    };
  },
  parsePageNumberPagination(url) {
    const args = url.slice(url.indexOf('?') + 1);
    const searchParams = new URLSearchParams(args);
    return searchParams.get('page');
  },
};
