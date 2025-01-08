The **Dyson equation** is a cornerstone in quantum field theory and condensed matter physics, describing how the Green's function (or propagator) of a system is modified due to interactions. Below is a detailed discussion of the Dyson equation, along with examples and solutions.

---

### **General Form of the Dyson Equation**
The Dyson equation relates the **interacting Green's function** \( G \) to the **non-interacting Green's function** \( G_0 \) and the **self-energy** \( \Sigma \):

\[
G = G_0 + G_0 \Sigma G
\]

#### Terms:
1. **\( G \)**: The full (interacting) Green's function.
2. **\( G_0 \)**: The free (non-interacting) Green's function.
3. **\( \Sigma \)**: The self-energy, which encodes all interaction effects.

#### Rearranging:
In frequency-momentum space, the Dyson equation can be written as:
\[
G^{-1}(k, \omega) = G_0^{-1}(k, \omega) - \Sigma(k, \omega)
\]
where \( G_0^{-1}(k, \omega) = \omega - \epsilon_k + i\eta \), with \( \epsilon_k \) being the energy dispersion of the non-interacting system.

---

### **Example 1: Single Particle in a Weakly Interacting System**

For a simple case of an electron interacting weakly with a system, the self-energy \( \Sigma \) can be computed perturbatively. Suppose:

- Non-interacting Green's function:
  \[
  G_0(k, \omega) = \frac{1}{\omega - \epsilon_k + i\eta}
  \]

- Self-energy (to first order in interaction \( V \)):
  \[
  \Sigma(k, \omega) = V^2 \frac{1}{\omega - \epsilon_k' + i\eta}
  \]

Then the full Green's function becomes:
\[
G(k, \omega) = \frac{1}{\omega - \epsilon_k - \Sigma(k, \omega) + i\eta}
\]
Substitute \( \Sigma(k, \omega) \):
\[
G(k, \omega) = \frac{1}{\omega - \epsilon_k - \frac{V^2}{\omega - \epsilon_k' + i\eta} + i\eta}
\]

This equation describes the modification of the particle's propagation due to interactions with the system.

---

### **Example 2: Phonon Interactions in Superconductors**

In the Bardeen-Cooper-Schrieffer (BCS) theory of superconductivity, the Dyson equation describes how electron Green's functions are modified by interactions with phonons.

1. **Non-interacting Green's function**:
   \[
   G_0(k, \omega) = \frac{1}{\omega - \epsilon_k + i\eta}
   \]

2. **Self-energy due to phonons**:
   \[
   \Sigma(k, \omega) = \int d\omega' \, \frac{\lambda}{\omega - \omega' + i\eta} \, G_0(k, \omega')
   \]
   where \( \lambda \) represents the electron-phonon coupling.

3. **Full Green's function**:
   The Dyson equation becomes:
   \[
   G(k, \omega) = \frac{1}{\omega - \epsilon_k - \Sigma(k, \omega) + i\eta}
   \]
   This equation can be solved iteratively or numerically to study superconducting states.

---

### **Solution Techniques**

#### **1. Iterative Approach**
The Dyson equation is often solved iteratively:
1. Start with an initial guess for \( G \), usually \( G = G_0 \).
2. Compute the self-energy \( \Sigma \) using \( G \).
3. Update \( G \) using:
   \[
   G = G_0 + G_0 \Sigma G
   \]
4. Repeat until convergence.

#### **2. Numerical Solution**
In more complex cases (e.g., lattice models), the Dyson equation is solved numerically using discretization of momentum and frequency spaces.

#### **3. Analytical Approximation**
For weak interactions or high symmetry, approximations such as perturbation theory or mean-field theory are used to simplify \( \Sigma \) and solve \( G \).

---

### **Example 3: Hubbard Model**
In the Hubbard model for strongly correlated electrons:

1. **Green's function**:
   \[
   G(k, \omega) = \frac{1}{\omega - \epsilon_k - \Sigma(k, \omega)}
   \]

2. **Self-energy from interactions**:
   The self-energy \( \Sigma \) is computed using methods like dynamical mean-field theory (DMFT), where:
   \[
   \Sigma(k, \omega) \approx \Sigma_{\text{local}}(\omega)
   \]
   This simplifies the Dyson equation in momentum space.

---

### **Summary**
The Dyson equation describes how interactions modify the propagation of particles or quasiparticles in a system. Its solutions provide key insights into quantum systems, including phenomena like quasiparticle behavior, superconductivity, and strong correlations. Solving the equation requires a combination of analytical approximations and numerical techniques, depending on the complexity of the self-energy \( \Sigma \).
