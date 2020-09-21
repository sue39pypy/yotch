export const state = () => ({
  accounts: [],       // SNSアカウント情報
  profile: []         // 名前等の基本的な情報
})

export const mutations = {
  // SNSアカウント情報をセット
  setAccounts (state, accounts) {
    state.accounts = accounts
  },

  // 基本情報をセット
  setProfile (state, profile) {
    state.profile = profile
  }
}

export const actions = {
  // 情報をセット
  async setInformation ({ commit }) {
    // 基本情報取得APIを呼び出し
    let url = '/api/informations/?type=profile'
    let response = await this.$axios.get(url)
    commit('setProfile', response.data.informations)

    // アカウント情報取得APIを呼び出し
    url = '/api/informations/?type=account'
    response = await this.$axios.get(url)
    commit('setAccounts', response.data.informations)
  }
}

export const getters = {
  getAccounts (state) {
    return state.accounts
  },

  getProfile (state) {
    return state.profile
  }
}