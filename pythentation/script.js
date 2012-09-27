		console.log('Init reveal');
		Reveal.initialize({
			// Display controls in the bottom right corner
			controls: true,

			// Display a presentation progress bar
			progress: true,

			// Push each slide change to the browser history
			history: false,

			// Enable keyboard shortcuts for navigation
			keyboard: true,

			// Enable the slide overview mode
			overview: true,

			// Loop the presentation
			loop: false,

			// Number of milliseconds between automatically proceeding to the 
			// next slide, disabled when set to 0
			autoSlide: 0,

			// Enable slide navigation via mouse wheel
			mouseWheel: true,

			// Apply a 3D roll to links on hover
			rollingLinks: true,

			// Transition style
			transition: 'default' // default/cube/page/concave/linear(2d)
		});
		console.log('Reveal inited');
