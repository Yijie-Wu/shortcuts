import {defineStore} from "pinia";

export const useAllKeysStore = defineStore('allKeysStore', {
    state() {
        return {
            keyboards: [],
        }
    },
    actions: {
        setKeys(data) {
            this.keyboards = data;
        }
    }
})
