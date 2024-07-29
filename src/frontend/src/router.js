import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

import Home from './components/page/Home'
import Search from "./components/page/Search";
import About from "./components/page/About";
import MyPage from "./components/page/MyPage";
import Login from "./components/page/Login";
import UserEdit from "./components/page/UserEdit";
import TeamEdit from "./components/page/TeamEdit";
import store from './vuex'

const router = new Router({
  mode: 'history',
  routes: [
    {
      name: 'home',
      path: '/',
      component: Home,
      meta: {
        requiresAuth: false
      }
    },
    {
      name: 'search',
      path: '/search',
      component: Search,
      meta: {
        requiresAuth: false
      }
    },
    {
      name: 'about',
      path: '/about',
      component: About,
      meta: {
        requiresAuth: false
      }
    },
    {
      name: 'my_page',
      path: '/my_page',
      component: MyPage,
      meta: {
        requiresAuth: true
      }
    },
    {
      name: 'login',
      path: '/login',
      component: Login,
      meta: {
        requiresAuth: false
      }
    },
    {
      name: 'user_add',
      path: '/user_add',
      component: UserEdit,
      meta: {
        requiresAuth: false
      }
    },
    {
      name: 'team_add',
      path: '/team_add',
      component: TeamEdit,
      meta: {
        requiresAuth: true
      }
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 };
  }
});

// ログイン認証はここで行う
router.beforeEach(async (to, from, next) => {
  if (!sessionStorage.getItem('ini')) {
    await store.commit('INI_ENCRYPT');
    await store.commit('RDS_ENCRYPT');
  } else if (from.name) {
    await store.commit('RDS_ENCRYPT');
  } else {
    await store.commit('RELOAD_STATE');
  }
  if (to.matched.some(record => record.meta.requiresAuth) && !sessionStorage.getItem('rda')) {
    next({path: '/'});
  } else {
    next()
  }
});
export default router
