import {defineStore} from "pinia";

export const useAllCategoryStore = defineStore('allCategoryStore', {
    state() {
        return {
            categories: [],
        }
    },
    actions: {
        setCategories(data) {
            this.categories = data;
        },
        addCategory(data) {
            this.categories.push(data);
        },
        updateCategory(data) {
            this.categories = this.categories.map(category => {
                if (category.id === data.id) {
                    return data;
                }
                return category;
            });
        },
        removeCategory(id) {
            this.categories = this.categories.filter(category => category.id !== id);
        },
    }
})
