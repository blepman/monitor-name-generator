#!usr/bin/env python3
from random import choice, randint

# This is an attempt to port the Halo monitor name generator at monitors.mradford.com to python
lnames = [
'symphony',
'augur',
'lance',
'nature',
'Identity',
'Series',
'Analogy',
'Bisect',
'Apex',
'Arc',
'Argument',
'Order',
'Asymptote',
'Autumn',
'Axes',
'Axiom',
'Axis',
'Balance',
'Bearing',
'Bias',
'Theorem',
'Bond',
'Boundary',
'Calculus',
'Capital',
'Coordinate',
'Centennial',
'Chord',
'Geometry',
'Circumference',
'Chorus',
'Testimony',
'Verdict',
'Closure',
'Cluster',
'Coefficient',
'Collateral',
'Column',
'Combination',
'Commission',
'Difference',
'Compass',
'Complement',
'Constant',
'Construction',
'Convergence',
'Prime',
'Correlation',
'Tangent',
'Cross',
'Integral',
'Density',
'Depth',
'Derivative',
'Determinant',
'Deviation',
'Dilation',
'Dimension',
'Direction',
'Distance',
'Divergence',
'Divide',
'Division',
'Divisor',
'Domain',
'Product',
'Double',
'Dozen',
'Edge',
'Element',
'Equal',
'Equality',
'Equation',
'Equinox',
'Equity',
'Error',
'Estate',
'Expense',
'Expression',
'Extrema',
'Focus',
'Formula',
'Theorem',
'Fractal',
'Fraud',
'Frequency',
'Polygon',
'Frustum',
'Sequence',
'Geometry',
'Gradient',
'Half',
'Harmony',
'Height',
'Helix',
'Hemisphere',
'Horizon',
'Hour',
'Hyperbola',
'Hypothesis',
'Identity',
'Inflation',
'Integral',
'Interest',
'Interval',
'Inverse',
'Operation',
'Naught',
'Limit',
'Locus',
'Arc',
'Axis',
'Matrix',
'Median',
'Minimum',
'Minuend',
'Mirror',
'Model',
'Multiple',
'Mile',
'Equal',
'Notation',
'Nought',
'Pattern',
'Sense',
'Theory',
'Obelus',
'Prism',
'Pyramid',
'Odds',
'Dimension',
'Interval',
'Sentence',
'Operation',
'Operator',
'Order',
'Ordinate',
'Origin',
'Symmetry',
'Series',
'Outcome',
'Outlier',
'Opal',
'Parallel',
'Parenthesis',
'Parity',
'Pattern',
'Deduction',
'Rank',
'Perimeter',
'Permutation',
'Perspective',
'Phase',
'Shift',
'Plane',
'Shape',
'Plot',
'Polygon',
'Position',
'Factor',
'Prime',
'Principal',
'Prism',
'Prophet',
'Projection',
'Proof',
'Proper',
'Proportion',
'Theorem',
'Quadrant',
'Quantity',
'Quarter',
'Quotient',
'Radian',
'Radical',
'Radius',
'Radix',
'Range',
'Return',
'Rationale',
'Reflection',
'Frequency',
'Rise',
'Rotation',
'Rule',
'Scale',
'Season',
'Secant',
'Sector',
'Segment',
'Sequence',
'Shape',
'Form',
'Solstice',
'Solution',
'Sphere',
'Spiral',
'Spring',
'Deviation',
'Notation',
'Substitution',
'Surface',
'Symbol',
'Tangent',
'Ternary',
'Tessellation',
'Theorem',
'Theory',
'Torus',
'Total',
'Translation',
'Transversal',
'Trust',
'Turn',
'Equal',
'Union',
'Bound',
'Variance',
'Vector',
'Vertex',
'Vertical',
'Wealth',
'Whole',
'Winter',
'Word',
'Champion',
'Zero',
'Cleric',
'Judgement',
'Emblem',
'Token',
'Impulse',
'Influence',
'Cause',
'Rationale',
'Sermon',
'Ritual',
'Fervor',
'Crusade',
'Verdict',
'Chorus',
'Radiance',
'Martyr',
'Conviction'
]

# https://www.thepersuasionrevolution.com/380-high-emotion-persuasive-words/

fnames = [
'objective',
'ardent',
'rational',
'ashen',
'charged',
'crimson',
'fervent',
'galvanic',
'transparent',
'jubilant',
'tragic',
'glorious',
'innocent',
'exuberant',
'blessed',
'genuine',
'radiant',
'hallowed',
'pious',
'righteous',
'noble',
'highborn',
'imperial',
'elite',
'absolute',
'stalwart',
'staunch',
'steadfast',
'supreme',
'cardinal',
'peerless',
'prevailing',
'fundamental',
'vital',
'paramount',
'foremost',
'aggressive',
'callous',
'compulsive',
'cunning',
'cynical',
'honest',
'dogmatic',
'obsessive',
'obstinate',
'critical',
'ruthless',
'stubborn',
'adaptable',
'adventurous',
'ambitious',
'amiable',
'amicable',
'brave',
'bright',
'calm',
'courageous',
'decisive',
'determined',
'diligent',
'discreet',
'dynamic',
'faithful',
'forceful',
'generous',
'gentle',
'gregarious',
'honest',
'impartial',
'independent',
'loyal',
'optimistic',
'patient',
'persistent',
'rational',
'confident',
'disciplined',
'sincere',
'straightforward',
'stoic',
'devout',
'malignant',
'malevolent',
'virulent',
'willing',
'recumbent',
'superior',
'desolate',
'incumbent',
'fawning',
'piercing',
'wicked'
]


from bottle import route, run
@route("/")
def page():
    num = randint(1, 1000)  # Generate a random number between 1 and 1000.
    fname = choice(fnames).capitalize()  # Pick a random name from fnames.
    lname = choice(lnames).capitalize()  # Pick random name from lnames.

    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <style type="text/css">
        .monitor-name { text-transform: capitalize; }
        body { background-color: #000; color: #fff; text-align: center; }
        .muted { color: #2bc7ca; }
    </style>
</head>
<body>
    <img src="https://www.halopedia.org/images/d/d5/Abject_Testament.jpg" alt="" width="200" height="150">	<h1 class="monitor-name">{num} {fname} {lname}</h1>	<button onclick="generateMonitorName()">Generate</button>	<br>	<br>	<br>	<a href="https://www.halopedia.org/Monitor" class="muted">wtf is a monitor?</a></body>
</html>
"""
run(host="localhost", port=8080, debug=True)
js = '''

function generateMonitorName()
{
  var num = Math.floor(Math.random() * 1000) + 1;
  var rand_math = math[Math.floor(Math.random() * math.length)];
  var rand_emotion = emotion[Math.floor(Math.random() * emotion.length)];

  document.getElementsByClassName('monitor-name')[0].innerHTML = num + ' ' + rand_emotion + ' ' + rand_math;
}
'''