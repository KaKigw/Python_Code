import streamlit as st
def Delta (a,b,c):
    delta = float(b)**2 - 4*float(a)*float(c)
    st.write("The value of Delta is:", delta)
    if delta > 0:
        st.write("The equation has two real roots.")
    elif delta == 0:
        st.write("The equation has one real root.")
    else:
        st.write("The equation has no real roots.")
    return delta

import cmath

def Roots(delta_value, a, b, c):
    # Format numbers nicely
    a_fmt, b_fmt, delta_fmt = f"{a:.2f}", f"{b:.2f}", f"{delta_value:.2f}"

    denominator = 2 * float(a)
    sqrt_delta = cmath.sqrt(delta_value)

    root1 = (-float(b) + sqrt_delta) / denominator
    root2 = (-float(b) - sqrt_delta) / denominator

    # Show roots numerically
    if delta_value > 0:
        st.write(f"✅ Two real roots: {root1.real:.2f} and {root2.real:.2f}")
        st.markdown(
            rf"$x = \frac{{-{b_fmt} \pm \sqrt{{{delta_fmt}}}}}{{2 \times {a_fmt}}} = \frac{{-{b_fmt} \pm {sqrt_delta.real:.2f}}}{{{denominator:.2f}}}$"
        )
    elif delta_value == 0:
        st.write(f"✅ One real root: {root1.real:.2f}")
        st.markdown(
            rf"$x = \frac{{-{b_fmt}}}{{2 \times {a_fmt}}} = \frac{{-{b_fmt}}}{{{denominator:.2f}}}$"
        )
    else:
        st.write(f"✅ Two complex roots: {root1:.2f} and {root2:.2f}")
        st.markdown(
            rf"$x = \frac{{-{b_fmt} \pm \sqrt{{{delta_fmt}}}}}{{2 \times {a_fmt}}} = \frac{{-{b_fmt} \pm {sqrt_delta:.2f}}}{{{denominator:.2f}}}$"
        )