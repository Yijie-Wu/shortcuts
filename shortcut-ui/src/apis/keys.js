import axios from '@/utils/request.js'


export function get_keys() {
    return axios(
        {
            method: 'get',
            url: '/keys/all',
        }
    )
}
