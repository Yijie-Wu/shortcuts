import {createRouter, createWebHashHistory} from 'vue-router';
import {showMessage} from "@/utils/message.js";

const routes = [
    {
        path: '/',
        name: 'Main',
        component: () => import('../views/main/MainView.vue'),
        meta: {'name': 'main'},
        children: [
            {
                path: '/',
                name: 'Index',
                component: () => import('../views/main/pages/Index.vue'),
                meta: {'name': 'index'},
            },
            {
                path: '/system/shortcuts',
                name: 'SystemShortcuts',
                component: () => import('../views/main/pages/SystemShortcuts.vue'),
                meta: {'name': 'system-shortcuts'},
            },
            {
                path: '/vscode/shortcuts',
                name: 'VscodeShortcuts',
                component: () => import('../views/main/pages/VscodeShortcuts.vue'),
                meta: {'name': 'vscode-shortcuts'},
            },
            {
                path: '/accotest/shortcuts',
                name: 'AccotestShortcuts',
                component: () => import('../views/main/pages/AccotestShortcuts.vue'),
                meta: {'name': 'accotest-shortcuts'},
            },
        ]
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes: routes,
});

export default router
