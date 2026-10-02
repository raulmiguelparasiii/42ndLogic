namespace OneLogic

universe u v o q r

abbrev Live (World : Type u) := World → Prop
abbrev Query (World : Type u) (Value : Type v) := World → Option Value
abbrev Transition (World : Type u) (Outcome : Type o) := World → Outcome → World → Prop

def NonemptyLive {World : Type u} (K : Live World) : Prop :=
  ∃ w, K w

def Categorical
    {World : Type u} {Value : Type v}
    (K : Live World) (query : Query World Value) (value : Value) : Prop :=
  NonemptyLive K ∧ ∀ w, K w → query w = some value

theorem greatestSoundCategorical
    {World : Type u} {Value : Type v}
    (K : Live World) (query : Query World Value)
    (R : Value → Prop)
    (hNonempty : NonemptyLive K)
    (hSound : ∀ value, R value → ∀ w, K w → query w = some value) :
    ∀ value, R value → Categorical K query value := by
  intro value hR
  exact ⟨hNonempty, hSound value hR⟩

def SharpUpdate
    {World : Type u} {Outcome : Type o}
    (K : Live World) (T : Transition World Outcome) (outcome : Outcome) : Live World :=
  fun after => ∃ before, K before ∧ T before outcome after

def UpdateSound
    {World : Type u} {Outcome : Type o}
    (K : Live World) (T : Transition World Outcome) (outcome : Outcome)
    (posterior : Live World) : Prop :=
  ∀ before after, K before → T before outcome after → posterior after

theorem sharpUpdateSound
    {World : Type u} {Outcome : Type o}
    (K : Live World) (T : Transition World Outcome) (outcome : Outcome) :
    UpdateSound K T outcome (SharpUpdate K T outcome) := by
  intro before after hK hT
  exact ⟨before, hK, hT⟩

theorem sharpUpdateSubsetOfEverySoundPosterior
    {World : Type u} {Outcome : Type o}
    (K : Live World) (T : Transition World Outcome) (outcome : Outcome)
    (posterior : Live World)
    (hSound : UpdateSound K T outcome posterior) :
    ∀ after, SharpUpdate K T outcome after → posterior after := by
  intro after hSharp
  rcases hSharp with ⟨before, hK, hT⟩
  exact hSound before after hK hT

theorem realityPreservedUnderFaithfulUpdate
    {World : Type u} {Outcome : Type o}
    (K : Live World) (T : Transition World Outcome)
    (actual actualNext : World) (outcome : Outcome)
    (hActual : K actual)
    (hReality : T actual outcome actualNext) :
    SharpUpdate K T outcome actualNext := by
  exact ⟨actual, hActual, hReality⟩

def Intersect {World : Type u} (K₁ K₂ : Live World) : Live World :=
  fun w => K₁ w ∧ K₂ w

theorem soundPooling
    {World : Type u}
    (K₁ K₂ : Live World) (actual : World)
    (h₁ : K₁ actual) (h₂ : K₂ actual) :
    Intersect K₁ K₂ actual := by
  exact ⟨h₁, h₂⟩

theorem soundPoolingNonempty
    {World : Type u}
    (K₁ K₂ : Live World) (actual : World)
    (h₁ : K₁ actual) (h₂ : K₂ actual) :
    NonemptyLive (Intersect K₁ K₂) := by
  exact ⟨actual, ⟨h₁, h₂⟩⟩

def Subset {World : Type u} (A B : Live World) : Prop :=
  ∀ w, A w → B w

theorem contractionCannotRepairExcludedActuality
    {World : Type u}
    (K K' : Live World) (actual : World)
    (hOut : ¬ K actual)
    (hSubset : Subset K' K) :
    ¬ K' actual := by
  intro hActual'
  exact hOut (hSubset actual hActual')

def ObservationUpdate
    {World : Type u} {Outcome : Type o}
    (K : Live World) (observe : World → Outcome) (outcome : Outcome) : Live World :=
  fun w => K w ∧ observe w = outcome

theorem observationPreservesActuality
    {World : Type u} {Outcome : Type o}
    (K : Live World) (observe : World → Outcome) (actual : World)
    (hActual : K actual) :
    ObservationUpdate K observe (observe actual) actual := by
  exact ⟨hActual, rfl⟩

theorem nondiscriminatingObservationNoInformation
    {World : Type u} {Outcome : Type o}
    (K : Live World) (observe : World → Outcome) (outcome : Outcome)
    (hSame : ∀ w, K w → observe w = outcome) :
    ∀ w, ObservationUpdate K observe outcome w ↔ K w := by
  intro w
  constructor
  · intro h
    exact h.1
  · intro h
    exact ⟨h, hSame w h⟩

theorem noFreeInformation
    {World : Type u}
    (K R : Live World)
    (hPreserve : ∀ w, K w → R w)
    (hNoInvent : ∀ w, R w → K w) :
    ∀ w, R w ↔ K w := by
  intro w
  constructor
  · exact hNoInvent w
  · exact hPreserve w

def SameQ
    {World : Type u} {Value : Type v} {QueryId : Type q}
    (admitted : QueryId → Prop)
    (evaluate : QueryId → World → Option Value)
    (a b : World) : Prop :=
  ∀ query, admitted query → evaluate query a = evaluate query b

def PreservesQueries
    {World : Type u} {Value : Type v} {QueryId : Type q} {Rep : Type r}
    (admitted : QueryId → Prop)
    (evaluate : QueryId → World → Option Value)
    (represent : World → Rep) : Prop :=
  ∀ a b, represent a = represent b → SameQ admitted evaluate a b

theorem mergingDifferentQuerySignaturesIsInadequate
    {World : Type u} {Value : Type v} {QueryId : Type q} {Rep : Type r}
    (admitted : QueryId → Prop)
    (evaluate : QueryId → World → Option Value)
    (represent : World → Rep)
    (a b : World)
    (hMerge : represent a = represent b)
    (hDifferent : ¬ SameQ admitted evaluate a b) :
    ¬ PreservesQueries admitted evaluate represent := by
  intro hPreserves
  exact hDifferent (hPreserves a b hMerge)

theorem modelClassFailureForcesExpansion
    {World : Type u}
    (modelClass K : Live World) (actual : World)
    (hOutside : ¬ modelClass actual)
    (hConfined : Subset K modelClass) :
    ¬ K actual := by
  intro hK
  exact hOutside (hConfined actual hK)

def UnsupportedExclusion
    {World : Type u} (ideal candidate : Live World) : Live World :=
  fun w => ideal w ∧ ¬ candidate w

def UnsupportedRetention
    {World : Type u} (ideal candidate : Live World) : Live World :=
  fun w => candidate w ∧ ¬ ideal w

def WeaklyDominates
    {World : Type u} (ideal better worse : Live World) : Prop :=
  Subset (UnsupportedExclusion ideal better) (UnsupportedExclusion ideal worse) ∧
  Subset (UnsupportedRetention ideal better) (UnsupportedRetention ideal worse)

def StrictlyDominates
    {World : Type u} (ideal better worse : Live World) : Prop :=
  WeaklyDominates ideal better worse ∧
  ((∃ w, UnsupportedExclusion ideal worse w ∧ ¬ UnsupportedExclusion ideal better w) ∨
   (∃ w, UnsupportedRetention ideal worse w ∧ ¬ UnsupportedRetention ideal better w))

def HasMaterialDeviation
    {World : Type u} (ideal candidate : Live World) : Prop :=
  NonemptyLive (UnsupportedExclusion ideal candidate) ∨
  NonemptyLive (UnsupportedRetention ideal candidate)

theorem idealWeaklyDominates
    {World : Type u}
    (ideal candidate : Live World) :
    WeaklyDominates ideal ideal candidate := by
  constructor
  · intro w h
    exact False.elim (h.2 h.1)
  · intro w h
    exact False.elim (h.2 h.1)

theorem idealStrictlyDominatesMaterialDeviation
    {World : Type u}
    (ideal candidate : Live World)
    (hDeviation : HasMaterialDeviation ideal candidate) :
    StrictlyDominates ideal ideal candidate := by
  constructor
  · exact idealWeaklyDominates ideal candidate
  · cases hDeviation with
    | inl hEx =>
        rcases hEx with ⟨w, hw⟩
        left
        refine ⟨w, hw, ?_⟩
        intro hImpossible
        exact hImpossible.2 hImpossible.1
    | inr hRet =>
        rcases hRet with ⟨w, hw⟩
        right
        refine ⟨w, hw, ?_⟩
        intro hImpossible
        exact hImpossible.2 hImpossible.1

theorem soundUpdateHasNoUnsupportedExclusion
    {World : Type u} {Outcome : Type o}
    (K : Live World) (T : Transition World Outcome) (outcome : Outcome)
    (posterior : Live World)
    (hSound : UpdateSound K T outcome posterior) :
    ∀ w, ¬ UnsupportedExclusion (SharpUpdate K T outcome) posterior w := by
  intro w hError
  exact hError.2 (sharpUpdateSubsetOfEverySoundPosterior K T outcome posterior hSound w hError.1)

theorem unsupportedExclusionMakesUpdateUnsound
    {World : Type u} {Outcome : Type o}
    (K : Live World) (T : Transition World Outcome) (outcome : Outcome)
    (posterior : Live World) (w : World)
    (hError : UnsupportedExclusion (SharpUpdate K T outcome) posterior w) :
    ¬ UpdateSound K T outcome posterior := by
  intro hSound
  exact hError.2 (sharpUpdateSubsetOfEverySoundPosterior K T outcome posterior hSound w hError.1)

theorem sharpUpdateStrictlyDominatesMaterialDeviation
    {World : Type u} {Outcome : Type o}
    (K : Live World) (T : Transition World Outcome) (outcome : Outcome)
    (posterior : Live World)
    (hDeviation : HasMaterialDeviation (SharpUpdate K T outcome) posterior) :
    StrictlyDominates (SharpUpdate K T outcome) (SharpUpdate K T outcome) posterior := by
  exact idealStrictlyDominatesMaterialDeviation (SharpUpdate K T outcome) posterior hDeviation

def InferenceOverreach
    {World : Type u} {Value : Type v}
    (K : Live World) (query : Query World Value) (R : Value → Prop) (value : Value) : Prop :=
  R value ∧ ¬ Categorical K query value

def InferenceOmission
    {World : Type u} {Value : Type v}
    (K : Live World) (query : Query World Value) (R : Value → Prop) (value : Value) : Prop :=
  Categorical K query value ∧ ¬ R value

theorem soundCategoricalRuleHasNoOverreach
    {World : Type u} {Value : Type v}
    (K : Live World) (query : Query World Value)
    (R : Value → Prop)
    (hNonempty : NonemptyLive K)
    (hSound : ∀ value, R value → ∀ w, K w → query w = some value) :
    ∀ value, ¬ InferenceOverreach K query R value := by
  intro value hOver
  exact hOver.2 (greatestSoundCategorical K query R hNonempty hSound value hOver.1)

def BridgeValid
    {World : Type u} {Value : Type v}
    (K : Live World)
    (premise conclusion : Query World Value)
    (premiseValue conclusionValue : Value) : Prop :=
  NonemptyLive (fun w => K w ∧ premise w = some premiseValue) ∧
  ∀ w, K w → premise w = some premiseValue → conclusion w = some conclusionValue

theorem liveCounterexampleDefeatsBridge
    {World : Type u} {Value : Type v}
    (K : Live World)
    (premise conclusion : Query World Value)
    (premiseValue conclusionValue : Value)
    (w : World)
    (hLive : K w)
    (hPremise : premise w = some premiseValue)
    (hConclusionFails : conclusion w ≠ some conclusionValue) :
    ¬ BridgeValid K premise conclusion premiseValue conclusionValue := by
  intro hBridge
  exact hConclusionFails (hBridge.2 w hLive hPremise)

end OneLogic
