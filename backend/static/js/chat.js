console.log("Chat with us.")

class WS  {
    constructor() {
        this.ws = new WebSocket(`ws://localhost:8000/chat/`);
        this.onmessage();
        // this.onclose();
    }


    async send(data) {
        const stringifiedData = JSON.stringify(data);
        this.ws.send(stringifiedData)
    }

    async onmessage(callback) {
        this.ws.onmessage = async (event) => {
            const li = document.createElement('li');
            const content = document.createTextNode(JSON.parse(event.data));
            li.appendChild(content);
            document.querySelector("#search-history").appendChild(li);
        }
    }
    async close() {
        this.ws.onclose = () => {
            console.log("ws Connection clonsed");
        }
    }

}

// websocket instance
const ws = new WS();

const search = async () => {
    document.querySelector("#search-button").onclick = async (e) => {
        const data = await ws.send(document.querySelector("#search-input").value)
    }
}

search();