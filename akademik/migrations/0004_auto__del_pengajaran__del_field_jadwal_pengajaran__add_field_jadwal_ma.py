# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Pengajaran'
        db.delete_table(u'akademik_pengajaran')

        # Deleting field 'Jadwal.pengajaran'
        db.delete_column(u'akademik_jadwal', 'pengajaran_id')

        # Adding field 'Jadwal.mata_pelajaran'
        db.add_column(u'akademik_jadwal', 'mata_pelajaran',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['akademik.MataPelajaran']),
                      keep_default=False)

        # Adding field 'Jadwal.kelas'
        db.add_column(u'akademik_jadwal', 'kelas',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['akademik.Kelas']),
                      keep_default=False)

        # Adding field 'Jadwal.pengajar'
        db.add_column(u'akademik_jadwal', 'pengajar',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['akademik.Guru']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Pengajaran'
        db.create_table(u'akademik_pengajaran', (
            ('pengajar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['akademik.Guru'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mata_pelajaran', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['akademik.MataPelajaran'])),
            ('kelas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['akademik.Kelas'])),
        ))
        db.send_create_signal(u'akademik', ['Pengajaran'])

        # Adding field 'Jadwal.pengajaran'
        db.add_column(u'akademik_jadwal', 'pengajaran',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['akademik.Pengajaran']),
                      keep_default=False)

        # Deleting field 'Jadwal.mata_pelajaran'
        db.delete_column(u'akademik_jadwal', 'mata_pelajaran_id')

        # Deleting field 'Jadwal.kelas'
        db.delete_column(u'akademik_jadwal', 'kelas_id')

        # Deleting field 'Jadwal.pengajar'
        db.delete_column(u'akademik_jadwal', 'pengajar_id')


    models = {
        u'akademik.guru': {
            'Meta': {'object_name': 'Guru'},
            'agama': ('django.db.models.fields.SmallIntegerField', [], {}),
            'aktif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alamat': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_kelamin': ('django.db.models.fields.SmallIntegerField', [], {}),
            'keterangan': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'mengajar': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['akademik.MataPelajaran']", 'symmetrical': 'False'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'nik': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'nomor_telepon': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'tanggal_lahir': ('django.db.models.fields.DateField', [], {})
        },
        u'akademik.jadwal': {
            'Meta': {'object_name': 'Jadwal'},
            'hari': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kelas': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Kelas']"}),
            'mata_pelajaran': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.MataPelajaran']"}),
            'mulai': ('django.db.models.fields.TimeField', [], {}),
            'pengajar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Guru']"}),
            'selesai': ('django.db.models.fields.TimeField', [], {})
        },
        u'akademik.jenisagenda': {
            'Meta': {'object_name': 'JenisAgenda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'akademik.jurusan': {
            'Meta': {'object_name': 'Jurusan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'akademik.kalenderakademik': {
            'Meta': {'ordering': "['-mulai', '-akhir']", 'object_name': 'KalenderAkademik'},
            'akhir': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_agenda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.JenisAgenda']"}),
            'keterangan': ('django.db.models.fields.TextField', [], {}),
            'mulai': ('django.db.models.fields.DateTimeField', [], {}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'akademik.kelas': {
            'Meta': {'object_name': 'Kelas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurusan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Jurusan']"}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'wali': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Guru']"})
        },
        u'akademik.matapelajaran': {
            'Meta': {'object_name': 'MataPelajaran'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurusan': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['akademik.Jurusan']", 'symmetrical': 'False'}),
            'nama': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'akademik.siswa': {
            'Meta': {'object_name': 'Siswa'},
            'agama': ('django.db.models.fields.SmallIntegerField', [], {}),
            'aktif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alamat': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_kelamin': ('django.db.models.fields.SmallIntegerField', [], {}),
            'kelas': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Kelas']"}),
            'keterangan': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'nis': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'nomor_telepon': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'tanggal_lahir': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['akademik']