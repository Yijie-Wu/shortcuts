import {defineStore} from "pinia";

export const useAllMouseStore = defineStore('allMouseStore', {
    state() {
        return {
            mouse: [],
        }
    },
    actions: {
        setMouse(data) {
            this.mouse = data;
        }
    }
})
