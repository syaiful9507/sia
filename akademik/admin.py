from django.contrib import admin

from .models import *


class GuruAdmin(admin.ModelAdmin):
    list_display = ['nik', 'nama', 'aktif']

    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-guru',),
            'fields': ['nik', 'aktif']
        }),
        ('Biodata', {
            'classes': ('suit-tab suit-tab-guru',),
            'fields': ['nama', 'jenis_kelamin', 'agama', 'tanggal_lahir']
        }),
        ('Kontak', {
            'classes': ('suit-tab suit-tab-guru',),
            'fields': ['alamat', 'email', 'nomor_telepon']
        })
    ]

    suit_form_tabs = (('guru', 'Guru'),)


class SiswaAdmin(admin.ModelAdmin):
    list_display = ['nis', 'nama', 'kelas', 'aktif']

    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-guru',),
            'fields': ['nis', 'kelas', 'aktif']
        }),
        ('Biodata', {
            'classes': ('suit-tab suit-tab-guru',),
            'fields': ['nama', 'jenis_kelamin', 'agama', 'tanggal_lahir']
        }),
        ('Kontak', {
            'classes': ('suit-tab suit-tab-guru',),
            'fields': ['alamat', 'email', 'nomor_telepon']
        })
    ]

    suit_form_tabs = (('guru', 'Guru'),)


class MataPelajaranAdmin(admin.ModelAdmin):
    list_display = ['nama']
    filter_horizontal = ['jurusan', 'pengajar']

    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-mata-pelajaran',),
            'fields': ['nama', 'jurusan', 'pengajar']
        }),
    ]

    suit_form_tabs = (('mata-pelajaran', 'Mata Pelajaran'),)


class JadwalAdmin(admin.ModelAdmin):
    list_display = ['kelas', 'mata_pelajaran', 'pengajar', 'hari', 'mulai', 'selesai']

    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-jadwal',),
            'fields': ['kelas', 'mata_pelajaran', 'pengajar', 'hari', 'mulai', 'selesai']
        }),
    ]

    suit_form_tabs = (('jadwal', 'Jadwal'),)


admin.site.register(Jurusan)
admin.site.register(Guru, GuruAdmin)
admin.site.register(Kelas)
admin.site.register(Siswa, SiswaAdmin)
admin.site.register(MataPelajaran, MataPelajaranAdmin)
admin.site.register(Jadwal, JadwalAdmin)
admin.site.register(JenisAgenda)
admin.site.register(KalenderAkademik)
