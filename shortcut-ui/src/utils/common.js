import {useAllKeysStore} from "@/stores/keys.js";
import {useAllMouseStore} from "@/stores/mouse.js";

let keys_store = useAllKeysStore()
let mouse_store = useAllMouseStore()


export function getKey(key_id) {
    for (const key of keys_store.keyboards) {
        if (key.id_ === String(key_id)) {
            return key.name1
        }
    }
}


export function getMouse(mouse_id) {
    for (let mouse of mouse_store.mouse) {
        if (mouse.id_ === String(mouse_id)) {
            return mouse.name
        }
    }
}
