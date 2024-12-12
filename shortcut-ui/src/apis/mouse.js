import axios from '@/utils/request.js'


export function get_mouse() {
    return axios(
        {
            method: 'get',
            url: '/mouse/all',
        }
    )
}
