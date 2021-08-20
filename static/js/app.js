//let form =  document.getElementsByTagName('form')[0]

document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */

      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      //window.location.href = 'http://127.0.0.1:8000/#help/?page='+page
      console.log(page);
    }
  }
  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }
  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();

    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          this.updateForm();
        });
      });

      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Send data to summary
    function sendData() {
    console.log('Sending data');
    let bags = document.getElementsByClassName('form-group form-group--inline')[0].firstElementChild.firstElementChild
    let street = document.getElementsByClassName('form-section--column')[0].firstElementChild.nextElementSibling
    let city = document.getElementsByClassName('form-section--column')[0].firstElementChild.nextElementSibling.nextElementSibling
    let code = document.getElementsByClassName('form-section--column')[0].firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling
    let phone = document.getElementsByClassName('form-section--column')[0].firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling

    let date = document.getElementsByClassName('form-section--column')[1].firstElementChild.nextElementSibling
    let time = document.getElementsByClassName('form-section--column')[1].firstElementChild.nextElementSibling.nextElementSibling
    let notes = document.getElementsByClassName('form-section--column')[1].firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling
    let orginization= document.getElementsByClassName('checkbox radio')
    let summary = document.getElementsByClassName('summary--text')

    bags.addEventListener('input', function (){
      summary[0].innerHTML=this.value + ' bags'
    })

    street.firstElementChild.children[1].addEventListener('input', function(){
      document.getElementsByClassName('form-section--column')[2].firstElementChild.nextElementSibling.firstElementChild.innerHTML= this.value
    })

    city.firstElementChild.children[1].addEventListener('input', function(){
      document.getElementsByClassName('form-section--column')[2].firstElementChild.nextElementSibling.firstElementChild.nextElementSibling.innerHTML=this.value
    })

    code.firstElementChild.children[1].addEventListener('input', function(){
      document.getElementsByClassName('form-section--column')[2].firstElementChild.nextElementSibling.firstElementChild.nextElementSibling.nextElementSibling.innerHTML=this.value
    })

    phone.firstElementChild.children[1].addEventListener('input', function(){
      document.getElementsByClassName('form-section--column')[2].firstElementChild.nextElementSibling.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.innerHTML=this.value
    })

    date.firstElementChild.children[1].addEventListener('input', function(){
      document.getElementsByClassName('form-section--column')[3].firstElementChild.nextElementSibling.firstElementChild.innerHTML=this.value
    })

    time.firstElementChild.children[1].addEventListener('input', function(){
     document.getElementsByClassName('form-section--column')[3].firstElementChild.nextElementSibling.firstElementChild.nextElementSibling.innerHTML=this.value
    })

    notes.firstElementChild.children[1].addEventListener('input', function(){
    document.getElementsByClassName('form-section--column')[3].firstElementChild.nextElementSibling.firstElementChild.nextElementSibling.nextElementSibling.innerHTML=this.value
    })

    for(let i=0; i<orginization.length; i++) {
      orginization[i].addEventListener('click', function (){
      console.log(i)
      })
    }

    let category = document.getElementsByClassName('form-group form-group--checkbox');
    let cat_values = []

    for(let i=0; i<7; i++) {
      category[i].firstElementChild.firstElementChild.addEventListener('change', function () {
      console.log(this.value)
    })
    }

  }
  sendData()

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));

    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

      // TODO: get data from inputs and show them in summary
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      e.preventDefault();
      this.currentStep++;
      this.updateForm();

      var formData = new FormData(this.$form.querySelector("form"))

 fetch("http://127.0.0.1:8000/add-donation/",
  {
        body: formData,
        headers: {'Authorization': 'Basic ' + btoa('login:password'), },
        method: "post",
        data: {
                 street : document.getElementsByClassName('form-section--column')[2].firstElementChild.nextElementSibling.firstElementChild.innerHTML,
               //  street : $('#street').val(),
                 csrfmiddlewaretoken: '{{ csrf_token }}',
                 dataType: "json",
                },
        success: function(data){
                   $('#output').html(data.msg) /* response message */
                },
      })
    .then((json) => json)
    .then((result) => {
      console.log('Success:', result);
      })
    .then((response)=>{
      window.location.href = "/confirmation/"
      })
    .catch(error => {
      console.error(error)
      });
    }
    }  // Formsteps


  const form = document.querySelector(".form--steps");

  if (form !== null) {
    new FormSteps(form);
  }
  else{
    console.log('form is empty')
  }
});