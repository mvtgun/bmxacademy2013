/*
---
description: native css animations.

license: MIT-style

authors:
- Thierry Bela

credits:
- amadeus (CSSEvents)
- André Fiedler, eskimoblood (Fx.Tween.CSS3)

requires:
core/1.3:
- Array
- Element.Style
- Fx.CSS

provides: [FxCSS]

...
*/

!function () {


	var set = Element.prototype.setStyle,
		get = Element.prototype.getStyle,
		//vendor = '',
		div = new Element('div'),
		prefix = Browser.safari || Browser.chrome || Browser.Platform.ios ? 'webkit' : (Browser.opera ? 'o' : (Browser.ie ? 'ms' : '')),
		prefixes = ['Khtml','Moz','Webkit','O','ms'];

	function getPrefix(prop) {

		//return unprefixed property if supported. prefixed properties sometimes do not work fine (MozOpacity is an empty string in FF4)
		if(prop in div.style) return prop;

		var upper = prop.charAt(0).toUpperCase() + prop.slice(1);

		for(var i = prefixes.length; i--;) if(prefixes[i] + upper in div.style) return prefixes[i] + upper;

		return prop;
	}

	Element.implement({

		setStyle: function (property, value) {

			return set.call(this, getPrefix(property), value);
		},
		getStyle: function (property) {

			return get.call(this, getPrefix(property));
		}
	});

	//eventTypes
	['transitionStart', 'transitionEnd'/* , 'animationStart', 'animationIteration', 'animationEnd' */].each(function(eventType) {

		Element.NativeEvents[eventType.toLowerCase()] = 2;

		var customType = eventType;

		if (prefix) customType = prefix + customType.capitalize();
		else customType = customType.toLowerCase();

		Element.NativeEvents[customType] = 2;
		Element.Events[eventType.toLowerCase()] = {base: customType }

	});

	//detect if transition property is supported
	Fx.css3Transition = (function (prop) {

		//
		if(prop in div.style) return true;

		var prefixes = ['Khtml','Moz','Webkit','O','ms'], upper = prop.charAt(0).toUpperCase() + prop.slice(1);

		for(var i = prefixes.length; i--;) if(prefixes[i] + upper in div.style) return true;

		return false
	})('transition');

	Fx.transitionTimings = {
		'linear'		: '0,0,1,1',
		'expo:in'		: '0.71,0.01,0.83,0',
		'expo:out'		: '0.14,1,0.32,0.99',
		'expo:in:out'	: '0.85,0,0.15,1',
		'circ:in'		: '0.34,0,0.96,0.23',
		'circ:out'		: '0,0.5,0.37,0.98',
		'circ:in:out'	: '0.88,0.1,0.12,0.9',
		'sine:in'		: '0.22,0.04,0.36,0',
		'sine:out'		: '0.04,0,0.5,1',
		'sine:in:out'	: '0.37,0.01,0.63,1',
		'quad:in'		: '0.14,0.01,0.49,0',
		'quad:out'		: '0.01,0,0.43,1',
		'quad:in:out'	: '0.47,0.04,0.53,0.96',
		'cubic:in'		: '0.35,0,0.65,0',
		'cubic:out'		: '0.09,0.25,0.24,1',
		'cubic:in:out'	: '0.66,0,0.34,1',
		'quart:in'		: '0.69,0,0.76,0.17',
		'quart:out'		: '0.26,0.96,0.44,1',
		'quart:in:out'	: '0.76,0,0.24,1',
		'quint:in'		: '0.64,0,0.78,0',
		'quint:out'		: '0.22,1,0.35,1',
		'quint:in:out'	: '0.9,0,0.1,1'
	};

	this.FxCSS = {

		Binds: ['onComplete'],
		initialize: function(element, options) {

			this.element = this.subject = document.id(element);
			this.parent(Object.merge({transition: 'sine:in:out'}, options));
			this.events = {transitionend: this.onComplete}
		},

		check: function() {

			if (this.css) {

				if(!this.locked && !this.running) return true
			}

			else if (!this.timer) return true;

			switch (this.options.link) {

				case 'cancel': this.cancel(); return true;
				case 'chain': this.chain(this.caller.pass(arguments, this)); return false;
			}

			return false;
		},

		onComplete: function () {

			//if(window.console && console.log) console.log(['completed', this.css]);
			if(this.css && this.running) {

				this.element.removeEvents(this.events).setStyle('transition', '');
				this.running = false
			}

			this.css = false;
			this.locked = false;

			return this.parent()
		},

		cancel: function() {

			if (this.css && this.running) {

				this.running = false;
				this.css = false
			}

			return this.parent()
		}
	}

}();

/*
---
description: css3 transform rule parser.

license: MIT-style

authors:
- Thierry Bela

credits:
- Pat Cullen (Fx.CSS.Transform)

requires:
core/1.3:
- Array
- Fx.CSS

provides: [Fx.CSS.Parsers.Transform]

...
*/

!function () {

	Number.implement({
		toRad: function() { return this * Math.PI/180; },
		toDeg: function() { return this * 180/Math.PI; }
	});

	Fx.CSS.implement({

		compute: function(from, to, delta) {

			var computed = [];

			from = Array.from(from);
			to = Array.from(to);
			(Math.min(from.length, to.length)).times(function(i){

				computed.push({value: from[i].parser.compute(from[i].value, to[i].value, delta), parser: from[i].parser});
			});
			computed.$family = Function.from('fx:css:value');
			return computed;
		},

		prepare: function(element, property, values) {

			values = Array.from(values);

			if (values[1] == null){

				values[1] = values[0];
				values[0] = element.getStyle(property);
			}

			var parser, parsed;

			if(property == 'transform') {

				parser = Fx.CSS.Parsers.Transform;
				parsed = values.map(function (value) { return {value: parser.parse(value), parser: parser} })
			}

			else parsed = values.map(this.parse);

			return {from: parsed[0], to: parsed[1]};
		}
	});

var deg = ['skew', 'rotate'],
	px = ['translate'],
	generics = ['scale'],
	coordinates = ['X', 'Y', 'Z'];

	px = px.concat(coordinates.map(function (side) { return px[0] + side }));
	generics = generics.concat(coordinates.map(function (side) { return generics[0] + side }));
	deg = deg.concat(coordinates.map(function (side) { return deg[0] + side })).concat(coordinates.map(function (side) { return deg[1] + side }));

	Object.merge(Fx.CSS.Parsers, {

		Transform: {

			parse: function(value){

				if(!value) return false;

				var transform = {};

				if(px.every(function (t) {

					if((match = value.match(new RegExp(t + '\\(\\s*([-+]?([0-9]*\\.)?[0-9]+)(px)?\\s*(,\\s*([-+]?([0-9]*\\.)?[0-9]+)(px)?\\s*)?\\)', 'i')))) {

						var x = parseFloat(match[1]),
							y = parseFloat(match[5]);

						//allow optional unit for 0
						if(!match[3] && x != 0) return false;

						if(match[4]) {

							if(!match[7] && y != 0) return false;
							transform[t] = [x, y]
						}

						else transform[t] = x
					}

					return true
				}) && deg.every(function (t) {

					if((match = value.match(new RegExp(t + '\\(\\s*([-+]?([0-9]*\\.)?[0-9]+)(deg|rad)?\\s*(,\\s*([-+]?([0-9]*\\.)?[0-9]+)(deg|rad)?)?\\s*\\)', 'i')))) {

						var x = parseFloat(match[1]),
							y = parseFloat(match[5]);

						//allow optional unit for 0
						if(!match[3] && x != 0) return false;
						if(match[4]) {

							if(!match[7] && y != 0) return false;
							transform[t] = [match[3] == 'rad' ? parseFloat(match[1]).toDeg() : parseFloat(match[1]), match[7] == 'rad' ? parseFloat(match[5]).toDeg() : parseFloat(match[5])]
						}

						else transform[t] = match[3] == 'rad' ? parseFloat(match[1]).toDeg() : parseFloat(match[1])
					}

					return true
				}) && generics.every(function (t) {

					if((match = value.match(new RegExp(t + '\\(\\s*(([0-9]*\\.)?[0-9]+)\\s*(,\\s*(([0-9]*\\.)?[0-9]+)\\s*)?\\)', 'i')))) {

						if(match[3]) transform[t] = [parseFloat(match[1]), parseFloat(match[4])];

						else transform[t] = parseFloat(match[1])
					}

					return true

				})) return Object.getLength(transform) == 0 ? false : transform;

				return false
			},
			compute: function(from, to, delta){

				var computed = {};

				Object.each(to, function (value, key) {

					if(value instanceof Array) {

						computed[key] = Array.from(from[key] == null ? value : Array.from(from[key])).map(function (val, index) {

							return Fx.compute(val == null ? value[index] : val, value[index], delta)
						})
					}

					else computed[key] = Fx.compute(from[key] == null ? value : from[key], value, delta)
				});

				return computed
			},
			serve: function(transform){

				var style = '';

				deg.each(function (t) {

					if(transform[t] != null) {

						if(transform[t] instanceof Array) style +=  t + '(' + transform[t].map(function (val) { return val + 'deg' }) + ') ';
						else style += t + '(' + transform[t] + 'deg) '
					}
				});

				px.each(function (t) { if(transform[t] != null) style += t + '(' + Array.from(transform[t]).map(function (value) { return value + 'px' }) + ') ' });
				generics.each(function (t) { if(transform[t] != null) style += t + '(' + transform[t] + ') ' });

				return style
			}
		}
	})
}();