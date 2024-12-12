import axios from '@/utils/request.js'


export function get_categories() {
    return axios(
        {
            method: 'get',
            url: '/category/all',
        }
    )
}

export function add_category(data) {
    return axios(
        {
            method: 'post',
            url: '/category/create',
            data
        }
    )
}

export function update_category(id, data) {
    return axios(
        {
            method: 'patch',
            url: `/category/update/${id}`,
            data
        }
    )
}

export function delete_category(id) {
    return axios(
        {
            method: 'delete',
            url: '/category/delete/' + id
        }
    )
}
