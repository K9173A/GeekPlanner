export default function parsePaginationURL(url) {
  const searchParams = new URLSearchParams(url);
  return {
    limit: searchParams.get('limit'),
    offset: searchParams.get('offset'),
  };
}
