# LeniTECH.K8s.Training
Kubernetes Basic Training - 3-Day Intensive

Ovo je prakticna obuka za Kubernetes. Ovaj repozitorijum sadrzi potrebne sablone, kodove i vezbe.

# Organizacija materijala
- 01-docker/: Osnove kontejnerizacije i build proces.
- 02-k8s-osnove/: Rad sa pod-ovima, Deploymentima i Servisima
- 03-konfiguracija/: ConfigMaps, Secrets i uvod u Helm
- 04-izazovi/: Prakticni zadaci sa namernim greskama za vezbu.

# Neophodni alati
Pre pocetka uverite se da imate instalirano:
- kubectl
- Ddocker Desktop
- git

# Podsetnik bitnih komandi
- kubectl get nodes | Provera statusa servera u klasteru
- kubectl apply -f [fajl] | Kreiranje ili azuriranje resursa
- kubectl get pods -w | Pracenje statusa pod-ova uzivo
- kubectl logs -f [ime-poda] | Citanje logova aplikacije
- kubectl describe [resurs] [ime] | Detaljna dijagnostika i Event-i
