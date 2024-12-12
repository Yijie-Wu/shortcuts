import axios from '@/utils/request.js'


export function get_vscode_shortcuts() {
    return axios(
        {
            method: 'get',
            url: '/shortcut/vscode/all',
        }
    )
}

export function get_system_shortcuts() {
    return axios(
        {
            method: 'get',
            url: '/shortcut/system/all',
        }
    )
}

export function get_accotest_shortcuts() {
    return axios(
        {
            method: 'get',
            url: '/shortcut/accotest/all',
        }
    )
}


export function create_accotest_shortcut(data) {
    return axios(
        {
            method: 'post',
            url: '/shortcut/accotest/create',
            data,
        }
    )
}

export function create_system_shortcut(data) {
    return axios(
        {
            method: 'post',
            url: '/shortcut/system/create',
            data,
        }
    )
}

export function create_vscode_shortcut(data) {
    return axios(
        {
            method: 'post',
            url: '/shortcut/vscode/create',
            data,
        }
    )
}


