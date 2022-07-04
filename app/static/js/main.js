((global) => {
    const API_URL = 'http://127.0.0.1:5000'
    let createBtnCurrentAction = 'CREATE';

    function main() {
        url.value = "";
        url.addEventListener('keyup', handleURLKeyPress);
        url.addEventListener('focusout', () => {
            if (url.value.trim() === "") {
                error.classList.add("hidden");
            }
        });

        const CREATE_BTN_ACTIONS = {
            CREATE: createShortURL,
            NEW: resetInput
        };


        create_btn.addEventListener("click", () => {
            CREATE_BTN_ACTIONS[createBtnCurrentAction]();

        })
    }

    function createShortURL() {
        create_btn.innerHTML = '<i data-feather="loader"></i>';
        feather.replace();
        create_btn.disabled = true;
        create_btn.classList.add("loader");
        document.querySelector(".url-input").classList.add("disabled");

        const data = new URLSearchParams();
        data.set("longurl", url.value);

        fetch(`${API_URL}/generate`, {
            method: "POST",
            body: data
        })
            .then(res => res.json())
            .then((response) => {
                if (response.error) {
                    document.querySelector(".shortened_url").classList.add("shortened_url_error");
                    document.querySelector(".shortened_url .text").innerText = response.error;
                    document.querySelector(".shortened_url").classList.add("appear");
                    return;
                }

                document.querySelector(".shortened_url").classList.remove("shortened_url_error");
                document.querySelector(".shortened_url a").innerText = response['url'];
                document.querySelector(".shortened_url a").href = response['url'];
                document.querySelector(".shortened_url").classList.add("appear");
                document.querySelector(".url-input").style.transform = 'translateY(-10px)'
            })
            .finally(() => {
                create_btn.innerText = 'new'
                create_btn.disabled = false;
                create_btn.classList.remove("loader");
                createBtnCurrentAction = 'NEW';
            })
    }

    function resetInput() {
        document.querySelector(".url-input").classList.remove("disabled");
        create_btn.innerText = 'create';
        createBtnCurrentAction = 'CREATE';
        url.value = "";
        url.focus();
        document.querySelector(".shortened_url").classList.remove("appear");
        document.querySelector(".url-input").style.transform = 'translateY(0)'

    }

    function handleURLKeyPress(event) {
        const url = event.target.value.trim();

        error.classList.add("hidden");
        create_btn.disabled = false;
        if (!isValidURL(url)) {
            error.classList.remove("hidden");
            create_btn.disabled = true;
        }
    }

    function isValidURL(string) {
        try {
            new URL(string);
            return true;
        } catch (_) {
            return false;
        }
    }

    document.addEventListener("DOMContentLoaded", main);
})(window);