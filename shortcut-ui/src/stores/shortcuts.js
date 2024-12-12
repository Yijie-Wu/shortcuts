import {defineStore} from "pinia";

export const useAllSystemShortcutStore = defineStore('allSystemShortcutStore', {
    state() {
        return {
            shortcuts: [],
        }
    },
    actions: {
        setShortcuts(data) {
            this.shortcuts = data;
        },
        addShortcut(data) {
            this.shortcuts.push(data);
        },
        updateShortcut(data) {
            this.shortcuts = this.shortcuts.map(shortcut => {
                if (shortcut.id === data.id) {
                    return data;
                }
                return shortcut;
            });
        },
        removeShortcut(id) {
            this.shortcuts = this.shortcuts.filter(shortcut => shortcut.id !== id);
        },
    }
})


export const useAllVscodeShortcutStore = defineStore('allVscodeShortcutStore', {
    state() {
        return {
            shortcuts: [],
        }
    },
    actions: {
        setShortcuts(data) {
            this.shortcuts = data;
        },
        addShortcut(data) {
            this.shortcuts.push(data);
        },
        updateShortcut(data) {
            this.shortcuts = this.shortcuts.map(shortcut => {
                if (shortcut.id === data.id) {
                    return data;
                }
                return shortcut;
            });
        },
        removeShortcut(id) {
            this.shortcuts = this.shortcuts.filter(shortcut => shortcut.id !== id);
        },
    }
})


export const useAllAccotestShortcutStore = defineStore('allAccotestShortcutStore', {
    state() {
        return {
            shortcuts: [],
        }
    },
    actions: {
        setShortcuts(data) {
            this.shortcuts = data;
        },
        addShortcut(data) {
            this.shortcuts.push(data);
        },
        updateShortcut(data) {
            this.shortcuts = this.shortcuts.map(shortcut => {
                if (shortcut.id === data.id) {
                    return data;
                }
                return shortcut;
            });
        },
        removeShortcut(id) {
            this.shortcuts = this.shortcuts.filter(shortcut => shortcut.id !== id);
        },
    }
})








