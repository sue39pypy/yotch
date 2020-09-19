export default async ({ store }) => {
  console.log('before dispatch')
  // フッターに表示するユーザー情報、SNS情報をstoreへ注入
  store.dispatch('information/setInformation', { root: true })
}