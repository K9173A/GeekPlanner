export default {
  accessTokenKey: 'jwtAccessToken',
  refreshTokenKey: 'jwtRefreshToken',

  /**
   * Gets current token from the web storage.
   * @param tokenKey - token name.
   * @returns {string} token.
   */
  get(tokenKey) {
    return localStorage.getItem(tokenKey);
  },
  /**
   * Deletes current token from the web storage.
   * @param tokenKey - token name.
   */
  delete(tokenKey) {
    localStorage.removeItem(tokenKey);
  },
  /**
   * Sets a new token to the storage.
   * @param tokenKey - token name.
   * @param newToken - new token.
   */
  save(tokenKey, newToken) {
    localStorage.setItem(tokenKey, newToken);
  },

  appendAuthHeaders(data) {
    const newData = data;
    if (!newData.headers) {
      newData.headers = {};
    }
    newData.headers.Authorization = `Bearer ${this.get(this.accessTokenKey)}`;
    return newData;
  },

  getAuthHeaders() {
    return {
      headers: {
        Authorization: `Bearer ${this.get(this.accessTokenKey)}`,
      },
    };
  },
};
